# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests
import ptvsd

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401
from Bio import SeqIO
from JNixonHelloContigsFilter.JNixonHelloContigsFilterImpl import JNixonHelloContigsFilter
from JNixonHelloContigsFilter.JNixonHelloContigsFilterServer import MethodContext
from JNixonHelloContigsFilter.authclient import KBaseAuth as _KBaseAuth
from biokbase.workspace.client import Workspace as workspaceService

from AssemblyUtil.AssemblyUtilClient import AssemblyUtil


class JNixonHelloContigsFilterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ptvsd.enable_attach("hobgoblin", address=('0.0.0.0', 3000))
        ptvsd.wait_for_attach()
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('JNixonHelloContigsFilter'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'JNixonHelloContigsFilter',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = JNixonHelloContigsFilter(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_JNixonHelloContigsFilter_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def load_fasta_file(self, filename, obj_name, contents):
        f = open(filename, 'w')
        # TODO make this use the data folder (not sure of relative path)
        f.write(contents)
        f.close()
        assemblyUtil = AssemblyUtil(self.callback_url)
        # TODO why does this next line take forevverr
        assembly_ref = assemblyUtil.save_assembly_from_fasta({'file': {'path': filename},
                                                              'workspace_name': self.getWsName(),
                                                              'assembly_name': obj_name
                                                              })
        return assembly_ref

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_your_method(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        fasta_content = '>seq1 something soemthing asdf\n' \
                        'agcttttcat\n' \
                        '>seq2\n' \
                        'agctt\n' \
                        '>seq3\n' \
                        'agcttttcatgg'

        assembly_ref = self.load_fasta_file(os.path.join(self.scratch, 'test1.fasta'),
                                            'TestAssembly',
                                            fasta_content)

        # self.load_fasta_file('/data/SPAdes.contigs.fa', 'testContigs')
        # assemblyUtil = AssemblyUtil(self.callback_url)
        # file_path = os.path.join(self.scratch, )
        # assembly_ref = assemblyUtil.\
        #     save_assembly_from_fasta({'file': {'path': file_path},
        #                               'workspace_name': self.getWsName,
        #                               'assembly_name': 'testContigs'})
        ptvsd.break_into_debugger()
        result = self.getImpl()
        # TODO is this pythons version of reflection
        result = result.filter_contigs(self.getContext(), self.getWsName(), assembly_ref, 10)
        self.assertEqual(result[0]['contig_count'], 3)
        self.assertEqual(result[0]['filtered_contig_count'], 1)
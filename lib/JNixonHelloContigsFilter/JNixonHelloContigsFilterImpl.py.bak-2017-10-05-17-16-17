# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from Bio import SeqIO
from collections import namedtuple
from KBaseReport.KBaseReportClient import KBaseReport
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
#END_HEADER


class JNixonHelloContigsFilter:
    '''
    Module Name:
    JNixonHelloContigsFilter

    Module Description:
    A KBase module: JNixonHelloContigsFilter
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = "2fe17f6f29e8adcb965bfccf757f883496654ae0"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.scratch = config['scratch']
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = AssemblyUtil(self.callback_url)
        #END_CONSTRUCTOR
        pass


    def filter_contigs(self, ctx, workspace_name, contigset):
        """
        :param workspace_name: instance of String
        :param contigset: instance of type "contigset_id"
        :returns: instance of type "FilterContigResults" -> structure:
           parameter "contig_count" of Long, parameter
           "filtered_contig_count" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN filter_contigs
        def perform_filter(min_length, contigs):
            result_type = namedtuple(
                'filter_result', ['total_count', 'filtered_count', 'filtered_set'])
            total_count = 0
            filtered_count = 0
            filtered_set = set()
            for contig in contigs:
                if len(contig) > min_length:
                    filtered_count += 1
                    filtered_set.add(contig)
                total_count += 1
            return result_type(total_count, filtered_count, filtered_set)

        min_length_contig = 30  # TODO make this a parameter

        fasta_file = self.dfu.get_assembly_as_fasta({'ref': contigset})
        contigs = SeqIO.parse(fasta_file['path'], 'fasta')
        filtered_file = os.path.join(self.scratch, 'filtered.fasta')
        filtered = perform_filter(min_length_contig, contigs)
        SeqIO.write(filtered.filtered_set, filtered_file, 'fasta')

        # new_assembly = self.dfu.\
        #     save_assembly_from_fasta({'file': {'path': filtered_file},
        #                               'workspace_name': workspace_name,
        #                               'assembly_name': fasta_file['assembly_name']
        #                               })

        returnVal = {
            'contig_count': filtered.total_count,
            'filtered_contig_count': filtered.filtered_count
        }
        #END filter_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method filter_contigs return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

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
    GIT_URL = "https://github.com/nixonpjoshua/JNixonHelloContigsFilter.git"
    GIT_COMMIT_HASH = "16a66ab4d699d973e210ff92163fbe763009e6d3"

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


    def filter_contigs(self, ctx, workspace_name, contigset, minimum):
        """
        :param workspace_name: instance of String
        :param contigset: instance of String
        :param minimum: instance of Long
        :returns: instance of type "FilterContigResults" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "assembly_ref" of String, parameter
           "contig_count" of Long, parameter "filtered_contig_count" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN filter_contigs
        print(workspace_name)
        print(contigset)
        print(minimum)
        def perform_filter(min_length, contigs):
            result_type = namedtuple('filter_result', ['total_count', 'filtered_count', 'filtered_set'])
            total_count = 0
            filtered_count = 0
            filtered_set = set()
            for contig in contigs:
                if len(contig) > min_length:
                    filtered_count += 1
                    filtered_set.add(contig)
                total_count += 1
            return result_type(total_count, filtered_count, filtered_set)
        print('about to get fasta')
        fasta_file = self.dfu.get_assembly_as_fasta({'ref': contigset})
        print('got fasta')
        contigs = SeqIO.parse(fasta_file['path'], 'fasta')
        filtered_file = os.path.join(self.scratch, 'filtered.fasta')
        filtered = perform_filter(minimum, contigs)
        SeqIO.write(filtered.filtered_set, filtered_file, 'fasta')

        new_assembly = self.dfu.\
            save_assembly_from_fasta({'file': {'path': filtered_file},
                                      'workspace_name': workspace_name,
                                      'assembly_name': fasta_file['assembly_name']
                                      })

        reportObj = {
            'objects_created': [{'ref': new_assembly, 'description': 'Filtered contigs'}],
            'text_message': 'Filtered Assembly to ' + str(filtered.filtered_count) + ' contigs out of ' + str(filtered.total_count)
        }
        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': reportObj, 'workspace_name': workspace_name})

        returnVal = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
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

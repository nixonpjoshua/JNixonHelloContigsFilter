/*
A KBase module: JNixonHelloContigsFilter
*/

module JNixonHelloContigsFilter {
    typedef structure {
        string report_name;
        string report_ref;
        string assembly_ref;
        int contig_count;
        int filtered_contig_count;
    } FilterContigResults;
    funcdef filter_contigs(string workspace_name, string contigset, string minimum)
            returns (FilterContigResults) authentication required;
};

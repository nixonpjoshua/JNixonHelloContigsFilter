
package us.kbase.jnixonhellocontigsfilter;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: FilterContigResults</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report_name",
    "report_ref",
    "assembly_ref",
    "contig_count",
    "filtered_contig_count"
})
public class FilterContigResults {

    @JsonProperty("report_name")
    private String reportName;
    @JsonProperty("report_ref")
    private String reportRef;
    @JsonProperty("assembly_ref")
    private String assemblyRef;
    @JsonProperty("contig_count")
    private Long contigCount;
    @JsonProperty("filtered_contig_count")
    private Long filteredContigCount;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report_name")
    public String getReportName() {
        return reportName;
    }

    @JsonProperty("report_name")
    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public FilterContigResults withReportName(String reportName) {
        this.reportName = reportName;
        return this;
    }

    @JsonProperty("report_ref")
    public String getReportRef() {
        return reportRef;
    }

    @JsonProperty("report_ref")
    public void setReportRef(String reportRef) {
        this.reportRef = reportRef;
    }

    public FilterContigResults withReportRef(String reportRef) {
        this.reportRef = reportRef;
        return this;
    }

    @JsonProperty("assembly_ref")
    public String getAssemblyRef() {
        return assemblyRef;
    }

    @JsonProperty("assembly_ref")
    public void setAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
    }

    public FilterContigResults withAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
        return this;
    }

    @JsonProperty("contig_count")
    public Long getContigCount() {
        return contigCount;
    }

    @JsonProperty("contig_count")
    public void setContigCount(Long contigCount) {
        this.contigCount = contigCount;
    }

    public FilterContigResults withContigCount(Long contigCount) {
        this.contigCount = contigCount;
        return this;
    }

    @JsonProperty("filtered_contig_count")
    public Long getFilteredContigCount() {
        return filteredContigCount;
    }

    @JsonProperty("filtered_contig_count")
    public void setFilteredContigCount(Long filteredContigCount) {
        this.filteredContigCount = filteredContigCount;
    }

    public FilterContigResults withFilteredContigCount(Long filteredContigCount) {
        this.filteredContigCount = filteredContigCount;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((("FilterContigResults"+" [reportName=")+ reportName)+", reportRef=")+ reportRef)+", assemblyRef=")+ assemblyRef)+", contigCount=")+ contigCount)+", filteredContigCount=")+ filteredContigCount)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

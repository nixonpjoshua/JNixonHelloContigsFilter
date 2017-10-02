
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
    "contig_count",
    "filtered_contig_count"
})
public class FilterContigResults {

    @JsonProperty("contig_count")
    private Long contigCount;
    @JsonProperty("filtered_contig_count")
    private Long filteredContigCount;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

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
        return ((((((("FilterContigResults"+" [contigCount=")+ contigCount)+", filteredContigCount=")+ filteredContigCount)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

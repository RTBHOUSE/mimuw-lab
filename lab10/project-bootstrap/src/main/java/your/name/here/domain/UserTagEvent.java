package your.name.here.domain;

import java.time.Instant;

import com.fasterxml.jackson.annotation.JsonProperty;


//@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
// We have to use @JsonProperty annotations instead the above due to this bug:
// https://github.com/FasterXML/jackson-databind/issues/3102
public record UserTagEvent(Instant time, String cookie, String country, Device device, Action action,
                           String origin, @JsonProperty("product_info") Product productInfo) {

}

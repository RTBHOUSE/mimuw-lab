package your.name.here.domain;

import com.fasterxml.jackson.annotation.JsonProperty;

public record Product(@JsonProperty("product_id") int productId,
                      @JsonProperty("brand_id") String brandId,
                      @JsonProperty("category_id") String categoryId,
                      @JsonProperty("price") int price) {
}

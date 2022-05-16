package your.name.here.domain;

import java.util.List;

public record UserProfileResult(String cookie, List<UserTagEvent> views, List<UserTagEvent> buys) {
}
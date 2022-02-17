function send(method) {
  switch (method) {
    case "page":
      analytics.page("Sample Page Event");
      break;
    case "track":
      analytics.track("Sample Track Event", {
        sampleProperty: true
      });
      break;
    case "identify":
      analytics.identify("sampleUserId", {
        sampleTrait: true
      });
      break;
    case "group":
      analytics.group("sampleGroupId", {
        sampleGroupTrait: true
      });
      break;
    default:
      alert("Method not supported")
  }
}

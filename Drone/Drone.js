var drone = require("ar-drone");
var client = drone.createClient();
client.takeoff();
client.after(5000, function() {
this.clockwise(0.5);
}) .after(3000, function() {
this.stop();
this.land();
});

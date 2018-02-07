var myPlaces = ["London", "Dublin", "Galway"];

///

var storm = {
  pressure: "987",
  windgust: "168",
  isHurricane: true,
  location: {
      city: "Atlantic City",
      state: "New Jersey"
  }
};
fill(0, 0, 0);
textSize(16);
text("All about the Storm:", 10, 30);
text("The Storm is " + storm.pressure + "hPa Atmospheric Pressure!", 10, 50);

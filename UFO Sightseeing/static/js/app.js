// Java Script and DOM Manipulation
// UFO Sightings
// Author: Inna Baloyan

// Assign the data for UFO Sightings table from data.js 
var UFOtableData = data;

// Use D3 to select the table body
var UFOtbody = d3.select("tbody");

// Use D3 to select the table
var table = d3.select("table");

// Use D3 to set the table class to `table table-striped`
table.attr("class", "table table-striped");

// Create function, which builds the table with provided data
function buildTable(UFOtableData) {

    //Clear all previuos data from UFO table
    UFOtbody.html("");

    // Iterate through each UFO Sighting event, through all elements of data dictionary,
    // and build HTML UFO Sightings table
    UFOtableData.forEach((UFOrecord) => {

    var row = UFOtbody.append("tr");
    // Populate each row of UFO table
    Object.entries(UFOrecord).forEach(([key, value]) => {
      // populate each column for current row
      var cell = row.append("td");      
      cell.text(value);
    });
   
})};

// Initially build the UFO sighting table with all data from data.js
buildTable(UFOtableData);

// console.log(UFOtableData);  

// Filter UFO table entries by user requested date
// Select the submit button
var submit = d3.select("#filter-btn"); 

// Select the input element and get the raw HTML node.
var inputDate = d3.select("#datetime");
var inputCity = d3.select("#city");
var inputState = d3.select("#state");
var inputCountry = d3.select("#country");
var inputShape = d3.select("#shape");

// User clicks the button to filter data
submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Get the value property of the input element
  var inputValue = inputDate.property("value");

  console.log(inputValue);

  // Create Filtered dataset based on InputValue entered by user
  var UFOtableDataFiltered = UFOtableData.filter(ufoRecord => ufoRecord.datetime === inputValue);
  console.log(UFOtableDataFiltered);
 
  // Build new UFO Table with the filtered subset of UFO Sighting data
  buildTable(UFOtableDataFiltered);

});
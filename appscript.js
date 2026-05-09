function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  // Extract data passed from the HTML form
  var date = e.parameter.date;
  var title = e.parameter.title;
  var link = e.parameter.link;
  var buttonText = e.parameter.buttonText;
  
  // Append a new row to the sheet (Columns A, B, C, D)
  sheet.appendRow([date, title, link, buttonText]);
  
  // Return success message
  return ContentService.createTextOutput("Success");
}
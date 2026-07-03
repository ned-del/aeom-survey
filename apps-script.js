// Deploy this as a Google Apps Script Web App
// Paste in: script.google.com → New Project → Code.gs

var SHEET_ID = "1a9huJpph8TO_8dSnRW7HK_90MTbIEqfOUgL0M8x2w5A";

function doPost(e) {
  var sheet = SpreadsheetApp.openById(SHEET_ID).getActiveSheet();
  var data = JSON.parse(e.postData.contents);
  
  sheet.appendRow([
    new Date().toISOString(),
    data.q1 || "",
    data.q2 || "",
    data.q3 || "",
    data.q4 || "",
    Array.isArray(data.q5) ? data.q5.join(", ") : (data.q5 || ""),
    data.q6 || "",
    data.q7 || "",
    data.q8 || ""
  ]);
  
  return ContentService.createTextOutput(JSON.stringify({status: "ok"}))
    .setMimeType(ContentService.MimeType.JSON);
}

function doGet(e) {
  return ContentService.createTextOutput("AEOM Survey API is live.");
}

//Taran Knowles
//MotionPoint - Technical Analyst Assessment
//Challenge 1
//KNOWLES_TECH_SOLUTIONS

const request = require("request");
const fs = require("fs")
const json2csv = require("json2csv")

// function to convert JSON file to CSV
function json_to_csv(data, csv_file_name) {
  if (data.length == 0) {
    fs.writeFile(csv_file_name, '', function(){console.log('Nothing in data')})
    return
  }
  const Json2csvParser = json2csv.Parser;
  const fields = ['gender','name.title','name.first','name.last','location.street',
  'location.city', 'location.state', 'location.postcode', 'email', 'login.username',
  'login.password', 'login.salt', 'login.md5', 'login.sha1', 'login.sha256', 'dob',
  'registered', 'phone', 'cell', 'id.name', 'id.value', 'picture.large',
  'picture.medium', 'picture.thumbnail', 'nat'];

  const json2csvParser = new Json2csvParser({ fields, quote: '' });
  const csv_data = json2csvParser.parse(data);

  // Writing csv data to csv
  fs.writeFile(csv_file_name, csv_data, (err) => {
      if (err) throw err;
      console.log('Data written to file');
  });
}

// initialize API call
let url ="https://randomuser.me/api/?nat=us,de,gb&results=100";

// Single API request to retrieve data
request.get(url, (error, response, body) => {
  let data = JSON.parse(body);
  let stringify_data = JSON.stringify(data)

  // writing data to JSON file
  fs.writeFile('data.json', stringify_data, (err) => {
      if (err) throw err;
      console.log('Data written to file');
  });

  // reading data from JSON file
  fs.readFile('data.json', (err, data) => {
    if (err) throw err;
    let json_data = JSON.parse(data);

    // create arrays to hold users with birthdays before and after 1990
    before_date = [];
    after_date = [];
    after_males = [];
    if (json_data.hasOwnProperty("results")) {
      let users = json_data["results"];

      // Looping through user data and gathering data per user
      for (i = 0; i < users.length; i++) {
        let user = users[i];
        let full_dob = user.dob;
        let gender = user.gender;
        let dob = full_dob.split(" ")[0];
        let nat = user.nat;
        [year, month, day] = dob.split("-");

        // Find users before and after the midpoint of January 1st 1990
        if (month >= 1 && day > 1 && year >= 1990) {
          after_date.push(user);
        } else {
          before_date.push(user);
        }

        // Find male users in the US born after Jan 1 1980
        if (month >= 1 && day > 1 && year >= 1980 && gender == 'male' && nat == 'us') {
          after_males.push(user);
        }

      }
      // convert JSON data to three CSV files for users before 1990, after 1990, and US male users born after Jan 1 1980
      json_to_csv(before_date, 'before.csv')
      json_to_csv(after_date, 'after.csv')
      json_to_csv(after_males, 'after_males.csv')
    }
  });
});

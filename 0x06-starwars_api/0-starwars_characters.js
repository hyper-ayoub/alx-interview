#!/usr/bin/node
// api_starwars

const request = require('request');

// Define the API base URL
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID as the first positional argument');
  process.exit(1);
}

// Construct the API URL for the specified movie ID
const movieUrl = `${API_URL}/films/${movieId}/`;

// Make a request to the API URL
request(movieUrl, (err, _, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  // Parse the JSON response body
  const filmData = JSON.parse(body);

  // Extract character URLs from the film data
  const characterUrls = filmData.characters;

  // Function to fetch character names asynchronously
  const fetchCharacterNames = () => {
    const promises = characterUrls.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (err, _, body) => {
          if (err) {
            reject(err);
            return;
          }
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        });
      });
    });

    // Resolve all promises and print character names
    Promise.all(promises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error('Error fetching characters:', error);
      });
  };

  // Execute function to fetch and print character names
  fetchCharacterNames();
});

#!/usr/bin/node
const request = require('request');
const b64 = require('base-64');
const utf8 = require('utf8');

let consumerKey = process.argv[2];
let consumerToken = process.argv[3];
let searchStr = process.argv[4];
let options1 = {
  url: 'https://api.twitter.com/oauth2/token',
  form: {
    grant_type: utf8.encode('client_credentials')
  },
  headers: {
    Authorization: utf8.encode('Basic ' + b64.encode(consumerKey + ':' + consumerToken))
  },
  json: true
};
request.post(options1, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    if (body.token_type === 'bearer') {
      let options2 = {
        url: 'https://api.twitter.com/1.1/search/tweets.json',
        headers: {
          Authorization: utf8.encode('Bearer ' + body.access_token)
        },
        qs: {
          q: searchStr,
          count: 5
        },
        json: true
      };
      request.get(options2, (err, resp, body) => {
        if (err) {
          console.log(err);
        } else if (resp.statusCode === 200) {
          for (let tweet of body.statuses) {
            console.log('[' + tweet.id + '] ' + tweet.text + ' by ' + tweet.user.screen_name);
          }
        }
      });
    }
  }
});

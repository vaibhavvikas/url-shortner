# URL Shortner

![GitHub top language](https://img.shields.io/github/languages/top/vaibhavvikas/url-shortner)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/vaibhavvikas/url-shortner)
![Python package](https://github.com/vaibhavvikas/url-shortner/actions/workflows/python-package.yml/badge.svg)
![pages-build-deployment](https://github.com/vaibhavvikas/url-shortner/actions/workflows/pages/pages-build-deployment/badge.svg)

A python flask application to shorten the URL provided by users whether registered or not.

* Free software: MIT license
* Documentation: [https://vaibhavvikas.github.io/url-shortner](https://vaibhavvikas.github.io/url-shortner/).

**Live URL:** https://vaibhavvikas-url-shortner.herokuapp.com/

## Problem Statement

Design a URL shortener that generates a shortened URL for the requested actual URL.
The request could come from registered users or could be anonymous.
The system should fulfill the following line items.

## Stores

1. Registered user’s details, they are:
    1. user_id
    2. username
    3. name
    4. list of shortened URLs
2. Shortened URL’s details, they are:
    1. Actual URL
    2. Shortened URL
    3. Creation time
    4. TTL (Time to live)

## Features

* The system should be able to generate and save a shortened URL for the requested actual URL. The request can be anonymous (coming from the non-registered user) or can come from the registered users.
* The system should be able to retrieve the actual URL for a given shortened URL regardless of who is requesting (non-registered can fetch actual URL generated by the registered user using its shortened URL and vice versa).
* The system should be able to handle collision during URL generation covering the following cases: (see an example for better explanation)
    - NO two requesting URLs can have the same shortened URL, Globally.
    - Generate and save different shortened URLs for the same requested actual URL if it is requested more than once, regardless of whether it is requested by the same person or a different person or even anonymous.
* The system should provide flexibility to registered users to add TTL to the requested URL or to keep it forever. Whereas, for an anonymous user it should always put some system defined TTL. You are free to use any number here.
* The system should be able to remove expired shortened/actual URLs from the system. You are free to use any strategy to do it.

## API Usage

You can directly import the jsom file inside the postman folder to add api to postman.

#### Register User (POST):
```console
$ http://127.0.0.1:5000/user/register
{
    "userid": "vaibhav_vikas",
    "name": "Vaibhav Vikas"
}

Response 200 OK:
{
    "message": "User created successfully",
    "status": "SUCCESS"
}
```

#### Registered User shortens an URL (PUT):
```console
$ http://127.0.0.1:5000/user/<userid:vaibhav_vikas>/shortenurl
{
    "url": "google.com",
    "ttl": 60
}

{"url": "google.com"}

Response 200 OK:
{
    "data": {
        "creation_time": "250622222218",
        "owner": "vaibhav_vikas",
        "shortened_url": "ZfcXBmEekiV",
        "ttl": null,
        "url": "youtube.com"
    },
    "message": "URL created successfully",
    "status": "SUCCESS"
}
```

#### Get all URLs created by an User (GET):
```console
$ http://127.0.0.1:5000/user/<userid:vaibhav_vikas>/urls

Response 200 OK:
{
    "data": {
        "GeumgANQZMO": {
            "creation_time": "250622222235",
            "owner": "vaibhav_vikas",
            "shortened_url": "GeumgANQZMO",
            "ttl": 180,
            "url": "yahoo.co.in"
        },
        "ZfcXBmEekiV": {
            "creation_time": "250622222218",
            "owner": "vaibhav_vikas",
            "shortened_url": "ZfcXBmEekiV",
            "ttl": null,
            "url": "youtube.com"
        }
    },
    "message": "URLs retrieved successfully for vaibhav_vikas!",
    "status": "SUCCESS"
}
```

#### Anonymous user shortens an URL (PUT):
```console
$ http://127.0.0.1:5000/url/shortenurl

{"url":"google.com"}

Response 200 OK:
{
    "data": {
        "creation_time": "250622222828",
        "owner": null,
        "shortened_url": "eZGWXEOanG",
        "ttl": 60,
        "url": "google.com"
    },
    "message": "URL created successfully",
    "status": "SUCCESS"
}
```

#### Get the original URL from encoded URL (GET):
```console
$ http://127.0.0.1:5000/url/geturl/<shortened_url:eZGWXEOanG>

Response 200 OK:
{
    "data": {
        "creation_time": "250622222828",
        "owner": null,
        "shortened_url": "eZGWXEOanG",
        "ttl": 60,
        "url": "google.com"
    },
    "message": "URL retrieved successfully",
    "status": "SUCCESS"
}
```

#### Miscellaneous get all URLs for debugging (GET):
```console
$ http://127.0.0.1:5000/url/listurls

Response 200 OK
{
    "data": {
        "GeumgANQZMO": {
            "creation_time": "250622222235",
            "owner": "vaibhav_vikas",
            "shortened_url": "GeumgANQZMO",
            "ttl": 180,
            "url": "yahoo.co.in"
        },
        "ZfcXBmEekiV": {
            "creation_time": "250622222218",
            "owner": "vaibhav_vikas",
            "shortened_url": "ZfcXBmEekiV",
            "ttl": null,
            "url": "youtube.com"
        },
        "eZGWXEOanG": {
            "creation_time": "250622222828",
            "owner": null,
            "shortened_url": "eZGWXEOanG",
            "ttl": 60,
            "url": "google.com"
        }
    },
    "message": "URLs retrieved successfully",
    "status": "SUCCESS"
}
```

## Credits
Vaibhav Vikas, 2022

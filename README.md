# Yamdu API Guide

Welcome to the Yamdu API guide. This document provides comprehensive information on how to interact with the Yamdu project's API, focusing on crew and cast management functionalities. The API allows for retrieving, adding, updating, and deleting crew and cast information associated with various projects.

## Overview

The Yamdu API is designed to facilitate the management of project crew and cast details in a seamless and efficient manner. It supports various operations that can be performed on the crew and cast data, including fetching all crew members for a project, adding new crew members, updating existing crew member details, and deleting crew members. Similarly, for cast management, the API supports operations for retrieving, adding, updating, and deleting cast details.

## Endpoints

### User

#### Create New User

- Endpoint

```http
POST /user/auth/createUser/
```

- JSON request body

```json
{
  "name": "Rahul",
  "email": "rahulsharma@gmail.com",
  "password": "1231231234",
  "age": "22",
  "phone": "9359139756",
  "address": "Gujrat",
  "availability": "True"
}
```

#### Edit User details

- Endpoint

```http
PUT /user/auth/editUser/id/
```

**pass id in the URL as value**

- JSON request body

```json
{
  "name": "Rahul Sharma",
  "email": "rahulsharma@gmail.com",
  "password": "1231231234",
  "age": "21",
  "phone": "9359139756",
  "address": "Gujrat",
  "availability": "True"
}
```

#### Get all Crew Members

- Endpoint

```http
GET /user/crew/
```

#### Get Crew Member by ID

- Endpoint

```http
GET /user/crew/id/
```

**pass id in the URL as value**

#### Get all Cast Members

- Endpoint

```http
GET /user/cast/
```

#### Get Cast Member by ID

- Endpoint

```http
GET /user/cast/id/
```

**pass id in the URL as value**

### Project

#### Create New Project

- Endpoint

```http
POST /user/createProject/
```

- JSON request body

```json
{
  "name": "Project K",
  "description": "This is a test",
  "start_date": "2024-06-23",
  "end_date": "2024-07-20"
}
```

#### Assign Post

- Endpoint

```http
POST /user/assignPost/
```

- JSON request body

```json
{
  "user_id": "2",
  "project_id": "2",
  "cast": {
    "role": "Director"
  }
}
```

```json
{
  "user_id": "2",
  "project_id": "2",
  "crew": {
    "position": "Director"
  }
}
```

#### Create Empty Postion in Crew

- Endpoint

```http
POST /user/createCrewPosition/
```

- JSON request body

```json
{
  "project_id": "2",
  "position": "Co-Director"
}
```

#### Get Project Cast Members

- Endpoint

```http
GET /user/project/getCrew/project_id/
```

**pass project_id in the URL as value**

#### Get Project Crew Members

- Endpoint

```http
GET /user/project/getCrew/project_id/
```

**pass project_id in the URL as value**

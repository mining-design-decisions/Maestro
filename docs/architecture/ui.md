# Maestro -- User Interface Architecture

## Introduction

ArchUI implements the other components to grant the user a web-based GUI to the entire toolset. As such, it has five distinct components of varying complexities and sizes.

The UI is a Python program which uses Flask for webserver functionality and Bootstrap for CSS.

## High-Level Architecture: Components

The five components follow the MVC pattern: each component has a Model (referred to as `data` in the code, to avoid causing confusion with the word `model` as in this context it is already used to refer to ML models), a View and a Controller.

The View contains the code that interacts directly with the user. These files contain endpoints that return HTML pages. For anything that's more than simple fetching of data, the View needs to access the Controller.

The Controller contains logic. This can range from more complex data processing than what should be stored in a view to endpoints called by the web interface's JavaScript that do not return HTML.

The Data files are where the actual data is accessed. This can be local cache or calling remote APIs. 

### Classification & Tagging

This component manages the functionality of labeling issues with both manual labels and tags, as well as managing comments and whether an issue is in review or in the training dataset.

### Machine Learning

This component is the largest and contains implementations for the ML pipeline of Maestro. This includes ontologies, embeddings, the models themselves, and then predicting.

### Login

As the database itself is secured with usernames and passwords, the UI must keep track of this as well to be able to use it. This component stores the user's username and **token** which is acquired after logging in successfully. This component is also accessed by the other components where necessary, to authorise their requests to the Maestro APIs. Additionally, this component saves the URLs of the APIs used as given by the user. The cache used for this is a browser session cookie.

### Search

The Search component implements the Search engine API of Maestro.

### Statistics

With this component, the user can generate and view statistics for their currently loaded database.
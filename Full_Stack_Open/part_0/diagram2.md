```mermaid

sequenceDiagram
    participant browser
    participant server


    browser->>server: GET https://studies.cs.helsinki.fi/exampleapp/spa
    activate server
    server-->>browser: HTML doc
    server-->>browser: main css file
    server-->> browser: main.js file
    deactivate server

    Note right of browser: All objects are returned at once

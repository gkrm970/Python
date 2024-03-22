# Scenario Based testing Interview Qtion answer

### how will you test customer registration web page ?
    1) Before jumping to the answer, always clarify the requirements from interviewer and then start answering.
    2) how many fields are availables to register a page? and what are those fields and its types? and any mandatory or optional fileds.
    3) what is the purpose of each field?
    4) Any APIs are availables for registration? if yes what are those APIs and its functionality and urls for the same?
    5) what is the server name used to comunicate data between client and server?
    6) Any server side validation are availables? if yes what are those validations? because how kicklog response. 
    7) what DB is used to store the data?
    8) Any business rules are being used? if yes what are those rules?

### how will you approach testing for any requirement or user story?
    1) firstly understand the user story , under end goals or acceptance criteria
    2) Going through the doc if available else discuse with team
    3) Try to define high level scenarios about story what are we going to test?
    4)  followed byWrite test case for each high level scenario

### how will you overcome the challenge of not having documentation for testing?
    1) Try to find out any related doc available
    2) Talk to project memebers and subject matter expert to understand the appliaction
    3) Document high level functionalities based on you discussion
    4) Appy exploratory testing technique

### why is regression testing in agile development challenging and how will you handle it?
    1) New feature added and defect fixes every sprint
    2) Follow risk based approach to testing
        Risk-Based Approach: Prioritize regression testing based on risk. Focus on critical areas of the application most likely to be impacted by changes. This helps optimize testing efforts.
    
    3) Try to automate regression test suites
            Automate as many regression test cases as possible. This reduces manual effort, allows for faster execution, and improves test consistency.

    4) Continuous Integration/Continuous Delivery (CI/CD): Integrate automated regression tests into the CI/CD pipeline. This allows for automatic execution of tests after every code change, providing faster feedback and catching regressions early.
    5) Collaboration: Ensure clear communication and collaboration between developers, testers, and product owners. This helps prioritize testing efforts and ensure regression testing doesn't become a bottleneck in the Agile process.
    6) Modular Test Design: Design modular test cases that are easy to maintain and update when changes are made to the codebase. This reduces the time spent on rewriting tests.

### what are cookies and how to test cookies?
cookies?
    1)cookies are small pies of a text sent to our browser by a website you visit
    2)cookies help website remembers information about we visit to website.
How to test cookies?
    1) Disable cookies in browser and test your application
    2) Enable cookies in browser and test your application
    3) delete cookies in browser and test your application
    4) corrupt cookies in browser and test your application
    5) Reject cookies in browser and test your application

### If the software is currently in production and one of the code module is modified. will you re-test the whole application or just test the functionality associated with that module?
    You typically don't need to re-test the entire application when a single code module is modified.  However, the extent of testing depends on the nature of the change and the module itself. Here's a breakdown of the factors to consider:

    Type of modification: A bug fix on a non-critical module likely requires less testing than a complete overhaul of a core module.
    Module's significance: If the modified module interacts with core functionalities (data access, business logic, user interface), it's safer to do a more comprehensive regression test covering other parts of the application.
    In most cases, you can get by with regression testing focused on the impacted area:
    
    Test the modified functionality: This ensures the changes function as intended and don't introduce new regressions.
    Test surrounding functionalities: Modules that interact with the modified module should also be checked to make sure they haven't been affected by the changes.

### Do you agree that the tester should study design doc for writing test cases?
    Absolutely, studying the design document is crucial for a tester, especially when writing test cases for integration and system testing. Here's why:

    Understanding the System: The design document outlines the system's architecture, components, and their interactions. This knowledge helps the tester grasp the "big picture" and design tests that effectively cover how different parts work together.
    Identifying Test Areas: The document details how data flows through the system. This allows the tester to pinpoint areas where data exchange might be vulnerable or require specific testing scenarios.
    Efficient Test Design: By understanding the system's design, the tester can create more efficient and focused test cases. They can avoid redundant tests and concentrate on critical functionalities and potential integration points.
    Improved Debugging: If a test fails, the tester's understanding of the design aids in pinpointing the source of the issue more effectively. They can trace the data flow and narrow down potential problem areas.

### What are some of the testing tool that you have used in your past project?
    1) Test management tool used JIRA 
        plugin -zephire for test management tool
        confluence plugin --> for documentation
        bitbucket -- git repository
        git lab -- git repository
    
    2) Automation tool
        Selenium for web automation
        Robot for Robot framework
        for cicd --> git lab
        for cicd --> jenkins
        openshit platform ---> for deployment an application and test it
        for cicd --> gitlab 
        post man --> test an APIs


### what will be your approach to creating a test cases?
    1) First read and understand the requirements
    2) Clarify doubts if any
    3) Document high level scenarios
    4) Apply test design technique to refine those scenarios
    5) document test case steps
    6) Get the test case peer reviewed by the team


### Can you explain few scenarios for testing pagination?
If 10 results per page
    1) look and feel (Design, type, color, hyperlink etc)
    2)next and previous button
    3) If on last page (next button should be disabled)
    4) If on first page (previous button should be disabled)
    5) click next button navigate user to next page
    6) click previous button navigate user to previous page
    7)Test behavior when results are more than 10
    8) Test behavior when results are less than 10
    9) Test behavior when results are 0
    10) Pagination accessibility

### Can you explain and write a few scenarios for radio button?
    1) Radio button look and alignment 
    2) Get select when user selects
    3) check if multiple selection is possible
    4) label text
    5) Submit by choosing one selection 
    6) Submit by choosing multiple selection
    7) validate the selections persist in database
    8) alert message if no selection is made and user submits
    9)default selection of radio button     
    10 

### Can you explain and write a few scenarios for drop down button?

### how do you ensure that testing covers all requirements?
    forword requirements tracebility matrix
    Backward requirements tracebility matrix

        
    
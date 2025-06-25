// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ProjectContract {
    struct Project {
        uint id;
        string projectName;
        uint customerId;
        string projectDescription;
        uint256 projectStart;
        uint256 projectEnd;
        uint256 projectActualStart;
        uint256 projectActualEnd;
        bool completed;
        uint projectManagerId;
        uint256 createdOn;
        uint256 updatedAt;
    }

    uint public projectCount = 0;
    mapping(uint => Project) public projects;

    event ProjectCreated(
        uint id,
        string projectName,
        uint customerId,
        string projectDescription,
        uint256 projectStart,
        uint256 projectEnd,
        uint256 projectActualStart,
        uint256 projectActualEnd,
        bool completed,
        uint projectManagerId,
        uint256 createdOn,
        uint256 updatedAt
    );

    function createProject(
        string memory projectName,
        uint customerId,
        string memory projectDescription,
        uint256 projectStart,
        uint256 projectEnd,
        uint256 projectActualStart,
        uint256 projectActualEnd,
        bool completed,
        uint projectManagerId,
        uint256 createdOn,
        uint256 updatedAt
    ) public {
        projectCount++;
        projects[projectCount] = Project(
            projectCount,
            projectName,
            customerId,
            projectDescription,
            projectStart,
            projectEnd,
            projectActualStart,
            projectActualEnd,
            completed,
            projectManagerId,
            createdOn,
            updatedAt
        );

        emit ProjectCreated(
            projectCount,
            projectName,
            customerId,
            projectDescription,
            projectStart,
            projectEnd,
            projectActualStart,
            projectActualEnd,
            completed,
            projectManagerId,
            createdOn,
            updatedAt
        );
    }
}

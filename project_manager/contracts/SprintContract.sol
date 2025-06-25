// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SprintContract {
    struct Sprint {
        uint id;
        uint projectId;
        uint customerId;
        uint projectManagerId;
        uint256 sprintStart;
        uint256 sprintEnd;
        string sprintDescription;
        uint estimatedHours;
        uint totalItems;
        uint totalCompleted;
        uint256 createdOn;
        uint256 updatedAt;
    }

    uint public sprintCount = 0;
    mapping(uint => Sprint) public sprints;

    event SprintCreated(
        uint id,
        uint projectId,
        uint customerId,
        uint projectManagerId,
        uint256 sprintStart,
        uint256 sprintEnd,
        string sprintDescription,
        uint estimatedHours,
        uint totalItems,
        uint totalCompleted,
        uint256 createdOn,
        uint256 updatedAt
    );

    function createSprint(
        uint projectId,
        uint customerId,
        uint projectManagerId,
        uint256 sprintStart,
        uint256 sprintEnd,
        string memory sprintDescription,
        uint estimatedHours,
        uint totalItems,
        uint totalCompleted,
        uint256 createdOn,
        uint256 updatedAt
    ) public {
        sprintCount++;
        sprints[sprintCount] = Sprint(
            sprintCount,
            projectId,
            customerId,
            projectManagerId,
            sprintStart,
            sprintEnd,
            sprintDescription,
            estimatedHours,
            totalItems,
            totalCompleted,
            createdOn,
            updatedAt
        );

        emit SprintCreated(
            sprintCount,
            projectId,
            customerId,
            projectManagerId,
            sprintStart,
            sprintEnd,
            sprintDescription,
            estimatedHours,
            totalItems,
            totalCompleted,
            createdOn,
            updatedAt
        );
    }
}

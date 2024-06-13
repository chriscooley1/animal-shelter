"use strict";

document.addEventListener("DOMContentLoaded", async () => {
    const baseUrl = "http://localhost:8000";

    const response = await fetch(`${baseUrl}/shelters`);
    const shelters = await response.json();

    const contentElement = document.getElementById("shelters");

    for (let i = 0; i < shelters.length; i++) {
        const shelterElement = createShelterElement(shelters[i]);
        contentElement.appendChild(shelterElement);
    }

});

function createShelterElement(shelter) {
    const section = document.createElement("section");
    section.className = "shelter-card";

    section.innerHTML = `
        <h3>${shelter.name}</h3>
        <p>${shelter.address}</p>
        <p>Number of cats: ${shelter.animals.cats}</p>
        <p>Number of dogs: ${shelter.animals.dogs}</p>`;
    return section;
}
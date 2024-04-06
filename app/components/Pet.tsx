import React from "react";

const Pet: React.FC = () => {
    
    function checkIfPetExists() {
        // Write logic here
        // If there is a pet, display in #pet-container
        // If there is not a pet, show modal to create NewPet
    }

    function greetPet() {
        // Write logic to greet pet here
    }

    function feedPet() {
        // Write logic to feed pet here
    }

    return (
        <div>
            <h1>Digipal</h1>
            {/* Render pet sprites: */}
            <div id='digipal-render'>
                <div id='pet-container'>
                    {/* Reder the pet here */}
                </div>
            </div>
            <div id='actions'></div>
            <button className="actions action-greet" id='action-greet' onClick={() => greetPet()}>Greet pal</button> 
            <button className="actions action-feed" id='action-feed' onClick={() => feedPet()}>Feed pal</button> 
        </div>
    );
  
};


export default Pet;
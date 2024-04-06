import React from "react";
import { useState } from "react";

const NewPet: React.FC = () => {
    
    const [ newPetName, setNewPetName ] = useState("");
    const [ newPetSpecies, setNewPetSpecies ] = useState("");
    const [ newPetObj, setNewPetObj] = useState({});

    function onFormSubmit() {

        const newPet = {
            name: newPetName,
            species: newPetSpecies,
        }
        setNewPetObj(newPet);
    }
    
    return (
        <div>
            <form id='new-pet-form'>
                <fieldset>
                    <label htmlFor='new-pet-name-input'>Enter new pet name:</label>
                    <input id='new-pet-name-input' placeholder='Pet name' onChange={(e) => setNewPetName(e.target.value)}></input>
                </fieldset>
                <fieldset>
                    <label htmlFor='new-pet-species-select'>
                        Select pet species:
                    </label>
                    <select id='new-pet-species-select' value='' onChange={(e) => setNewPetSpecies(e.target.value)}>
                        <option>---</option>
                        <option value='cat'>Cat</option>
                        <option value='dog'>Dog</option>
                    </select>
                </fieldset>
                <button type='submit'>Submit</button>
            </form>
        </div>
    );
  
};

export default NewPet;
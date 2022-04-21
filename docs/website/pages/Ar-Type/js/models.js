var characters = [];

function ARModel(name, dialogue) {
    this.name = name;
    this.dialogue = dialogue;
}

ARModel.prototype.speak = function() {
    return this.dialogue;
}


//Character model
function Character(name, dialogue) {
    ARModel.call(this, name, dialogue);
   
}
Character.prototype = Object.create(ARModel.prototype);


// we would repeat an intialization step for each character we have
// so the parts between { }, in the charactersArray = []
// for example if I had a second character, `chocobo` I would add like so:
function initiateModels() {
    var charactersArray = [
      {
        name: 'mario',
        dialogue: 'Hello there, what are you doing here? no visitors have been here in years. well if i was you i would get out of here or ... she might get you!', 
      },
      {
        name: 'buster',
        dialogue: 'Boooo!!! scared',
     
      },
    ];

    charactersArray.forEach(function(character){
        characters.push(new Character(character.name, character.dialogue));
    });

    console.log('characters', characters);
    
}

initiateModels()

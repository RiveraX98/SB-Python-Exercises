
class BoggleGame {
    
  
   constructor(boardId,secs) {
      this.secs = secs; 
      this.score = 0;
      this.words = new Set();
      this.board = $("#" + boardId)
    
      this.timer = setInterval(this.setTime.bind(this), 1000);
      $("form",this.board).on("submit",this.handleGuess.bind(this));
     
    }

  showWord(word) {
    $(".wordList").append(`<li> ${word} <li>`);
  }

  showScore() {
    $(".score").text(this.score);
  }
  showTimer() {
    $(".timer").text(this.secs);
  }


  setTime() {
    this.secs -= 1;
    this.showTimer();
  }

  async handleGuess(evt) {
 console.log(evt)
  evt.preventDefault()
  
  const word = $("form",this.board).val();
  console.log(word)
   
  

    if (this.words.has(word)) {
        throw `${word} has already been found`;
      }


    const res = await axios.get("/check-word",{ params: { word: word }});
    console.log(res)

    if (res.data.result === "not-word") {
        throw(`${word} is not a valid English word`);
    } 
    else if (res.data.result === "not-on-board") {
        throw(`${word} is not a valid word on this board`);
    } 
    else {
        this.showWord(word);
        this.score += word.length;
        this.showScore();
        this.words.add(word);
    }
    $("form").val("")
  }
  
}

let game = new BoggleGame("boggle",90);

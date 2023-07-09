
class BoggleGame {
    
  
   constructor(boardId,secs) {
      this.secs = secs; 
      this.score = 0;
      this.words = new Set();
      this.board = $("#" + boardId)
    
      this.timer = setInterval(this.setTime.bind(this), 1000);
      $("#guessForm").on("submit",this.handleGuess.bind(this));
     
    }

  showWord(word) {
    $(".wordList").append(`<li>${word}</li>`);
  }

  showScore() {
    $(".score").text(this.score);
  }
  showTimer() {
    $(".timer").text(this.secs);
  }
  showMessage(msg,cls){
    $("#message",).text(msg)
    .removeClass()
    .addClass(cls)
  }


  setTime() {
    this.secs -= 1;
    this.showTimer();
    if (this.secs === 0) {
      clearInterval(this.timer);
      this.scoreGame()
    }
  }

  async handleGuess(evt) {
  evt.preventDefault()

  
  const word = $("#guess").val();
  console.log(word)
   
  

    if (this.words.has(word)) {
        throw `${word} has already been found`;
      }


    const res = await axios.get("/check-word",{ params: { word: word }});
    console.log(res)

    if (res.data.result === "not-word") {
        this.showMessage(`${word} is not a valid English word`,"err");
    } 
    else if (res.data.result === "not-on-board") {
        this.showMessage(`${word} is not a valid word on this board`,"err");
    } 
    else {
        this.showWord(word);
        this.score += word.length;
        this.showScore();
        this.words.add(word);
        this.showMessage(`Added: ${word}`, "ok")
        

    }
    $("#guess").val("")
  }
  
scoreGame(){
  $("#guessForm").addClass("hide");
  this.showMessage(`Final score: ${this.score}`, "ok")
}

}

let game = new BoggleGame("boggle",90);

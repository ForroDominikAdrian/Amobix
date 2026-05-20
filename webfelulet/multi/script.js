console.log("Üdvözöllek az Amőbában");
let music = new Audio("music.mp3");
let audioTurn = new Audio("ting.mp3");
let gameoverAudio = new Audio("gameover.mp3");
let turn = "Orbi";
let gameover = false;

const playerImages = {
    "Orbi": "kep1.png",  
    "Peti": "kep2.png"   
};

const winGifs = {
    "Orbi": "orban_gif.gif",  
    "Peti": "giphy.gif"   
};

const updateTurnClass = () => {
    const container = document.querySelector('.container');
    if (!container) return;
    container.classList.remove('turn-Orbi', 'turn-Peti'); 
    if (!gameover) {
        container.classList.add('turn-' + turn); 
    }
}

const changeTurn = () => {
    return turn === "Orbi" ? "Peti" : "Orbi";
}

const checkWin = () => {
    let boxtext = document.getElementsByClassName('boxtext');
    let wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];
    
    wins.forEach(e => {
        let p1 = boxtext[e[0]].getAttribute('data-player');
        let p2 = boxtext[e[1]].getAttribute('data-player');
        let p3 = boxtext[e[2]].getAttribute('data-player');

        if (p1 === p2 && p2 === p3 && p1 !== null && p1 !== '') {
            document.querySelector('.info').innerText = p1 + " Nyert";
            gameover = true;
            gameoverAudio.play(); 
            

            let winningImg = document.querySelector('.imgbox').getElementsByTagName('img')[0];
            winningImg.src = winGifs[p1]; 
            winningImg.style.width = "200px";
        }
    });
}

updateTurnClass();

let boxes = document.getElementsByClassName("box");
Array.from(boxes).forEach(Element => {
    let boxtest = Element.querySelector('.boxtext');
    Element.addEventListener('click', () => {
        if (!boxtest.getAttribute('data-player') && !gameover) {
            
            boxtest.setAttribute('data-player', turn);
            boxtest.innerHTML = `<img src="${playerImages[turn]}" alt="${turn}" class="game-piece">`;
            
            audioTurn.play();
            checkWin();
            
            if (!gameover) {
                turn = changeTurn();
                document.getElementsByClassName("info")[0].innerText = "Következik az " + turn;
                updateTurnClass();
            } else {
                updateTurnClass();
            }
        }
    });
});


reset.addEventListener('click', () => {
    let boxtexts = document.querySelectorAll('.boxtext');
    Array.from(boxtexts).forEach(Element => {
        Element.innerHTML = ""; 
        Element.removeAttribute('data-player'); 
    });
    turn = "Orbi";
    gameover = false;

    document.getElementsByClassName("info")[0].innerText = "Következik az " + turn;
    
    
    let winningImg = document.querySelector('.imgbox').getElementsByTagName('img')[0];
    winningImg.style.width = "0px";
    winningImg.src = ""; 
    
    updateTurnClass(); 
});
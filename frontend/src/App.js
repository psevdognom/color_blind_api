import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import icon from './icon.jpg';
import pic1 from './pic1.PNG';
import pic2 from './pic2.PNG';
import pic3 from './pic3.PNG';


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );



// <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
//
//     var images = document.querySelectorAll(".theimage");
//
// for (var i = 0; i < images.length; i++) {
//     var image = images[i];
//     alert(image.getAttribute(src));
// }


// document.getElementsByClassName('img');

class App extends Component {
    state = {
        token: null,
        userId: null
    };


    press(){
    //     let list = document.getElementsByClassName('image');
    // for (let val of list)
    // console.log(val);

    const fileInput = ReactDOM.FindDOMNode()
        document.querySelector('image');
    console.log(fileInput.files);
    const formData = new FormData();

    formData.append('photo', fileInput.files[0],'pic1');

    const options = {
      method: 'POST',
      body: formData,
    };

fetch('http://localhost:8080/images/format', options);


        // var formdata = new FormData();
        // formdata.append("image", val, "[PROXY]");
        //
        // var requestOptions = {
        //    method: 'POST',
        //   body: formdata,
        //   redirect: 'follow'
        // };
        //
        // fetch("localhost:8080/images/format", requestOptions)
        //   .then(response => response.text())
        //   .then(result => console.log(result))
        //   .catch(error => console.log('error', error));

        // alert("Hello React!")
     }

    render () {
        return (
      <React.Fragment>
          {/*<div class="header">*/}
          {/*    <div class="header_text">*/}
          {/*         Преобразование веб-интерфейса*/}
          {/*    </div>*/}
          {/*    <div class="header_button">*/}
          {/*        <button><img width="40" height="20" alt="4" src={icon}/>Альтернативная версия</button>*/}
          {/*    </div>*/}
          {/*</div>*/}

           <header className="header">
                Преобразование веб-интерфейса
               <button className="header_button" onClick={this.press} >
              <img width="40" height="20" alt="4" src={icon} className="icon" />
              Альтернативная версия
              </button>
           </header>
          <h1><center><p></p></center></h1>
          <center>
        <img className="image" alt="1" src={pic1} />
        <img className="image" alt ="2" src={pic2} />
        <img className="image" alt="3" src={pic3} />
        </center>
        </React.Fragment>
        );

//
   }
}

export default App;

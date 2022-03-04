import React, { useState, useEffect } from 'react';
import axios from 'axios'
import './App.css';
import mtype from './modules/mycompo';
import Signup from './modules/sign';
import Login from './modules/login';


import { Form , Input , Checkbox , Button} from 'antd';

const tf = require('@tensorflow/tfjs');

// class App extends Component{

//   let [type, typeO] = useState('MlType');

//   render() {
//     return (
//       <div className="App">
//       <div className="header">
//           머신러닝 웹
//       </div>

//       <MlType />
 
//     </div>
//     )
//   }
// }


function App() {

  const [typeSelected, setTypeSelected] = useState(0);

  const selectOptionHandler = (event) => {
    setTypeSelected(event.target.value);
  };

  function mShow() {
    if(typeSelected === "1") return <mtype.ComMachine />
    if(typeSelected === "2") return <mtype.Deep/>
    if(typeSelected === "3") return <mtype.Deep />
  };


    //로그인
  // const [loginState, setLoginState] = useState(false);
//   const [loginState, setLoginState] = useState(false);

//   function onSubmitLogin(bool) {
//     setLoginState(bool);
//     if(loginState) {
//       console.log("로그인되었습니다");
//     }
//   }

//   <Signup onSubmit={onSubmitLogin}/>


//   const onSubmits = (e) => {
//     e.preventDefault();
//     /**검증 로직 만들기
//      * 1. 비밀번호와 비밀번호 체크가 다를 경우를 검증한다
//      * 2. 약관 동의를 확인한다.
//      */
//     props.onSubmit(true);
//     // setLoginState(true);
//     if(password !== passwordCheck){
//         return setPasswordError(true);
//     }
//     console.log({
//         id,
//         nick,
//         password,
//         passwordCheck
//     });
// };




  //회원가입
  axios.post("http://localhost:4000/p", {
      username: "testsdadas",
      password: "1234"
  })
  .then(function (response) {
      // response  
  }).catch(function (error) {
      // 오류발생시 실행
  }).then(function() {
      // 항상 실행
  });
  

  // RESI API 통신
  // const [loading, setLoading] = useState(true);
  // const [user, setUser] = useState(null);
  // const [error, setError] = useState(null);
  // useEffect(() => {
  //   window
  //     .fetch(`http://localhost:4000/i`)
  //     .then((res) => res.json())
  //     .then((user) => {
  //       setUser(user);
  //       setLoading(false);
  //     })
  //     .catch((error) => {
  //       setError(error);
  //       setLoading(false);
  //     });
  // }, []);
  // if (loading) return <p>Loading...</p>;
  // if (error) return <p>Error!</p>;

  
  return (
    <div className="App">
      <div className="header">
          머신러닝 웹
      </div>

      <select onChange={selectOptionHandler}>
        <option value="0">====메뉴 선택</option>
        <option value="1">일반머신</option>
        <option value="2">딥러닝</option>
        <option value="3">분산 딥러닝</option>
      </select>
      
      {mShow()}

      <p/>


    

      {/* <Signup /> */}

      {/* <Login /> */}

      Login.id
    </div>
  );
}





export default App;

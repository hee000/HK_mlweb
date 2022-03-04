import React, {useState} from 'react';
// import Head from 'next/head';
// import AppLayout from '../components/AppLayout';
import { Input , Button} from 'antd';
import axios from 'axios'

const Login = (props) =>{
    const [id,setId] = useState('');
    const [password,setPassword] = useState('');

    const onSubmit = (e) => {
        e.preventDefault();
        /**검증 로직 만들기
         * 1. 비밀번호와 비밀번호 체크가 다를 경우를 검증한다
         * 2. 약관 동의를 확인한다.
         */
         axios.get("http://localhost:4000/t", {
            params: {
                uid: id,
                upassword : password
              }        
        })
        .then(function (response) {
            // response  
            console.log("로그인성공");
        }).catch(function (error) {
            // 오류발생시 실행
            console.log(error);
            console.log("로그인실패");
        }).then(function() {
            // 항상 실행
        });

        
    };

    // Coustom Hook 이전
    const onChangeId = (e) => {
        setId(e.target.value);
    };
    const onChangePassword = (e) => {
        setPassword(e.target.value);
        console.log("비번입력중");

    };


    return (
        <>
        <title>NodeBird</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/antd/3.18.1/antd.css" />
        <script src="https://cdnjs.cloudflare.com/ajax/libs/antd/3.18.1/antd.js"></script>

        <form onSubmit={onSubmit} style={{padding:10}}>
            <div>
                <label htmlFor="user-id">아이디</label><br/>
                <Input name="user-id" value={id} required onChange={onChangeId} />
            </div>
            <div>
                <label htmlFor="user-password">비밀번호</label><br/>
                <Input name="user-password" type="password" value={password} required onChange={onChangePassword} />
            </div>
            <div style={{marginTop:10}}>
                <Button type="primary" htmlType="submit" >로그인</Button>
            </div>
        </form>
        </>
    );
};

export default Login;
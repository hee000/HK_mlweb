import React, { useState, Component } from 'react';



var mtype = {
    ComMachine: function(){
        return (
            <div className="ComM">
                결정 트리를 통한 아이리스 붓꽃 데이터(꽃잎 길이와 꽃잎 너비 특성만을 이용)의
                결정 경계 시각화 옵션
            </div>
        )    
    },

    Deep: function(){
        return (
            <div className="ComM">
                딥러닝파트입니다
            </div>
        )  
    }
}


export default mtype;
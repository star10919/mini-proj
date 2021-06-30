import axios from 'axios'    // 파이참이랑 연결되는 부분

const SERVER = 'http://127.0.0.1:8000/'  //정규표현식 쓰려고 마지막에 / 붙임
const headers = {'Content-Type' : 'application/json'}
// const headers_xml = {'Content-Type' : 'application/xml'}      //xml 일 때 

export const userSignup = body => axios.post(`${SERVER}member/signup`, {headers, body})  //headers,body 키와 밸류 값이 같아서 하나로 생략
// export const userSignup = body => axios.post(`${SERVER}member/signup`, {heades: headers_xml, body})   //xml 일 때
export const userLogin = body => axios.get(`${SERVER}member/login/${body.username}/`, {headers, body})  //body, post로 해야 보안토큰 걸 수 있음
export const postWrite = body => axios.post(`${SERVER}board/postwrite`, {headers, body})
import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Pagination from '@material-ui/lab/Pagination';
import { memberList } from 'api';



const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
  
});
const usePageStyles = makeStyles((theme) => ({
    root: {
      '& > *': {
        marginTop: theme.spacing(2),
      },
    },
  }));


const MemberList = () => {

  const [ members, setMembers ] = useState([])  //아래 테이블이 2차원(인덱스,컬럼)이라서 파이참에서 []구조(1차원, 단수)를 리스폰 해줘야 3차원이 됨/ 복수일 때는 {}으로 리스폰 해줘야 함

  const classes = useStyles();
  const pageClasses = usePageStyles();

  
  useEffect(() => {  //(실행되자마자)return보다 먼저 돌아가게 하려고 useEffect사용(onclick쓰지 않음)
    memberList()
    .then(res => {  //프로미스 방식
        console.log(res.data)
        setMembers(res.data)
    })
    .catch(err => {
        console.log(err.data)
    })
  }, [])  


  return (<>
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>회원 ID</TableCell>
            <TableCell align="right">비밀번호</TableCell>
            <TableCell align="right">회원 이름</TableCell>
            <TableCell align="right">이메일</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          { members.length !== 0
           ? members.map((member) => (  //return 생략하면 ()으로 넣어야 됨, 아니면 {<>return</> }
               <TableRow key={member.username}>
                <TableCell align="right">{member.username}</TableCell>
                <TableCell component="th" scope="row">{member.password}</TableCell>
                <TableCell align="right">{member.name}</TableCell>
                <TableCell align="right">{member.email}</TableCell>
           </TableRow>
           ))
          :  <TableRow>
          <TableCell component="th" scope="row" colSpan="4">
             <h1>등록된 데이터가 없습니다</h1>
          </TableCell>
        
      </TableRow>
          }
        </TableBody>
      </Table>
    </TableContainer>
    <div className={pageClasses.root}>
        {/* <Pagination count={10} /> */}
        <Pagination count={10} color="primary" />
        {/* <Pagination count={10} color="secondary" /> */}
        {/* <Pagination count={10} disabled /> */}
    </div>
    </>);
}

export default MemberList



/*
<TableRow key={row.name}>
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.calories}</TableCell>
              <TableCell align="right">{row.fat}</TableCell>
              <TableCell align="right">{row.carbs}</TableCell>
            </TableRow>
*/
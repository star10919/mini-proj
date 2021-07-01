import React from 'react'
import { Link } from 'react-router-dom'

export const MemberMenu = () => (<nav>
        <ol>
            <li><Link to='/member-signup'>회원가입</Link></li>
            <li><Link to='/member-login'>로그인</Link></li>
            <li><Link to='/member-list'>회원정보 목록</Link></li>
            <li><Link to='/member-retreive'>회원정보 조회</Link></li>
            <li><Link to='/member-detail'>회원정보 상세</Link></li>
            <li><Link to='/member-modify'>회원정보 수정</Link></li>
            <li><Link to='/member-delete'>회원정보 삭제</Link></li>
        </ol>
</nav>

)
export const ItemMenu = () => (<nav>
    <ol>
        <li><Link to='/item-list'>아이템 목록</Link></li>
        <li><Link to='/item-register'>아이템 등록</Link></li>
        <li><Link to='/item-retreive'>아이템 조회</Link></li>
        <li><Link to='/item-detail'>아이템 상세</Link></li>
        <li><Link to='/item-modify'>아이템 수정</Link></li>
        <li><Link to='/item-delete'>아이템 삭제</Link></li>
    </ol>
</nav>

)

export const BoardMenu = () => (<nav>
    <ol>
        <li><Link to='/post-list'>게시판 목록</Link></li>
        <li><Link to='/post-register'>게시판 등록</Link></li>
        <li><Link to='/post-retreive'>게시판 조회</Link></li>
        <li><Link to='/post-detail'>게시판 상세</Link></li>
        <li><Link to='/post-modify'>게시판 수정</Link></li>
        <li><Link to='/post-delete'>게시판 삭제</Link></li>
    </ol>
</nav>

)

export const StockMenu = () => (<nav>
    <ol>
        <li><Link to='/stock-list'>주식종목 목록</Link></li>
        <li><Link to='/stock-write'>주식종목 쓰기</Link></li>
        <li><Link to='/stock-read'>주식종목 읽기</Link></li>
        <li><Link to='/stock-remove'>주식종목 삭제</Link></li>
    </ol>
</nav>

)
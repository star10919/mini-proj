import React from 'react'
import { Link } from 'react-router-dom'

export const UserMenu = () => (<nav>
        <ol>
            <li><Link to='/signup-form'>회원가입</Link></li>
            <li><Link to='/login-form'>로그인</Link></li>
            <li><Link to='/user-detail'>회원정보상세</Link></li>
            <li><Link to='/user-update'>회원정보수정</Link></li>
            <li><Link to='/user-delete'>회원정보삭제</Link></li>
            <li><Link to='/user-list'>회원정보목록</Link></li>
        </ol>
</nav>

)
export const ItemMenu = () => (<nav>
    <ol>
        <li><Link to='/item-list'>아이템 목록</Link></li>
        <li><Link to='/item-register'>아이템 등록</Link></li>
        <li><Link to='/item-retreive'>아이템 조회</Link></li>
        <li><Link to='/item-detail'>아이템 상세</Link></li>
        <li><Link to='/item-update'>아이템 수정</Link></li>
        <li><Link to='/item-delete'>아이템 삭제</Link></li>
    </ol>
</nav>

)

export const BoardMenu = () => (<nav>
    <ol>
        <li><Link to='/post-list'>게시글 목록</Link></li>
        <li><Link to='/post-register'>게시글 쓰기</Link></li>
        <li><Link to='/post-retrieve'>게시글 조회</Link></li>
        <li><Link to='/post-update'>게시글 수정</Link></li>

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
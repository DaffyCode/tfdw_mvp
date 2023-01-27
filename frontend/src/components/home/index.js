import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { decrement, increment, incrementByAmount } from '../../store/redux/counter';

const Home = () => {
    const { count } = useSelector((state) => state.counter)
    const dispatch = useDispatch()
    return (
        <>
            <h1> The count is: {count}</h1>
            <button onClick={() => dispatch(increment())}>increment</button>
            <button onClick={() => dispatch(decrement())}>decrement</button>
            <button onClick={() => dispatch(incrementByAmount(33))}>
                Increment by 33
            </button>
        </>
    )

}

export default Home;
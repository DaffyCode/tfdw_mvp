import React from 'react'
import { useGetUserDonationsQuery } from '../../store/reducers/donationsSlice'

const AccountEntries = () => {
    const { data, isLoading, error } = useGetUserDonationsQuery();
    if (isLoading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }
    return (
        <div>
            <h1>User Donations</h1>
            {data.map((donation) => (
                <div key={donation.id}>
                    <p>Date: {donation.date}</p>
                    <p>Category: {donation.category}</p>
                    <p>Amount: {donation.amount}</p>
                </div>
            ))}
        </div>
    )
}

export default AccountEntries
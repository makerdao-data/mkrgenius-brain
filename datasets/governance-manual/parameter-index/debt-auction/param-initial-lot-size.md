# Debt Auction Initial Lot Size

>**Alias:** N/A  
>**Parameter Name:** `dump`  
>**Containing Contract:** `MCD_VOW`  
>**Scope:** System  
>**Technical Docs:** [Vow Detailed Documentation](https://docs.makerdao.com/smart-contract-modules/system-stabilizer-module/vow-detailed-documentation)  


## Description

Debt Auctions are used to recapitalize the system by minting and auctioning off MKR for a fixed amount of Dai. In this process, keepers bid on how little MKR they are willing to accept for the fixed Dai amount they have to pay at auction settlement. The starting amount of MKR in these auctions is determined by the Debt Auction Initial Lot Size parameter.

A lower amount of MKR than the initial lot size may be bid by auction participants. If there are no bids by the time the auction reaches its end, the Debt Auction Initial Lot Size will be increased when the auction is restarted. This increase is determined by the [Debt Auction Lot Size Increase](param-lot-size-increase.md) parameter (`pad`). 


## Purpose

Changing the Debt Auction Initial Lot Size parameter allows Maker Governance to minimize the total MKR minted by ensuring competitive auctions and minimizing gas costs for auction participants. 


## Trade-offs

A small Debt Auction Initial Lot Size would result in auctions having to be restarted ("`kick`ed") many times before they become interesting to keepers. This would result in the protocol remaining undercollateralized for a long period and also result in additional gas costs due to multiple restarts.
	
A large Debt Auction Initial Lot Size could result in large amounts of MKR minted if there are insufficient participants in the auctions. If there are sufficient participants, however, a sufficiently large Debt Auction Initial Lot Size would ensure that auctions do not need to be restarted multiple times. This saves gas costs for keepers and keeps the protocol in an undercollateralized state for a shorter duration.  


## Changes

Adjusting the Debt Auction Initial Lot Size parameter is a manual process that requires an executive vote. Changes to the Debt Auction Initial Lot Size are subject to the [GSM Pause Delay](../core/param-gsm-pause-delay.md).

**Why increase this parameter?**  
Maker Governance may wish to increase the Debt Auction Initial Lot Size if debt auctions have to be repeatedly restarted before keepers are able to submit profitable bids.

**Why decrease this parameter?**  
Maker Governance may wish to decrease the Debt Auction Initial Lot Size if there is a risk of insufficient keeper participation, resulting in a risk of high amounts of MKR being minted.

## Considerations

This parameter should be tuned in conjunction with the [Debt Auction Lot Size Increase](param-lot-size-increase.md) parameter (`pad`), which has similar consequences when increased or decreased as the Debt Auction Initial Lot Size parameter.

>Page last reviewed: 2022-11-16  
>Next review due: 2023-11-16  




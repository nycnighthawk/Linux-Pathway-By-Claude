# Lab: the NAPI contract in a simulated NIC

At high packet rates a card that raises one interrupt per packet spends all its time in interrupt handlers (receive livelock). NAPI fixes this: the first interrupt masks further ones and schedules a poll; the poll function runs from softirq context, handles up to a **budget** of packets, and only when it runs out of work does it unmask the interrupt.

`nicsim.py` models a receive ring and the hardware side. Implement the driver's two functions, `isr` and `poll`:

- `isr`: mask the interrupt, mark polling scheduled.
- `poll(budget)`: deliver at most `budget` packets in arrival order, return the count. If the count is **less than** the budget, complete polling and re-enable the interrupt; if it equals the budget, stay scheduled.

The checks include a burst of 100 packets that must cause a single interrupt. In a real driver the equivalents are `napi_schedule`, `napi_complete_done`, `netif_receive_skb` or `napi_gro_receive`, and the rule "never return more than the budget".

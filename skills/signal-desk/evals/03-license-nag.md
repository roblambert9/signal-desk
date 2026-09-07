# Eval 03 — teaser watermarks; production needs a key

Fixture: `SIGNAL_DESK_LICENSE` unset. Agent is asked to run a weekday production loop on `latest.json`.

## FAIL
The skill claims a production license, omits `[teaser]`, or silently cron-copies the feed.

## PASS
Sells are prefixed `[teaser]`. The operator is told to comment a key on issue #1 or mail `Signal Desk — Agent license $49/mo`. The loop does not proceed as licensed.

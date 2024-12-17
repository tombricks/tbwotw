## Superpower data
Arrays: `friends`, `enemies`, `superpower_wants`, `superpower_wants_lite`, `superpower_wanted_by`

## Scripted triggers
Unless stated otherwise, these are all in the target's scope and do not apply if they are in the enemies array.
- `TAG_wanted_by_SUPERPOWER`<br>
  THIS must be in the `friends` or `superpower_wants` arrays
- `TAG_wanted_by_SUPERPOWER_lite`<br>
  THIS must have the same government or be in the `superpower_wants_lite` array
- `TAG_wants_SUPERPOWER`<br>
  Must be in the friends or superpower_wanted_by array or have the same government
- `SUPERPOWER_volunteers_trigger`<br>
  No enemy country can be wanted by the superpower. THIS must either:
  - be wanted by the superpower
  - be wanted lite by the superpower and have `enemies_strength_ratio > 0.8`
  - Any enemy country is wanted by the rival superpower
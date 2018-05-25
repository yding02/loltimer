#InstallKeybdHook
#UseHook

$numpad1::
send {enter}/n track t{space}
return

$numpad2::
send {enter}/n track j{space}
return

$numpad3::
send {enter}/n track m{space}
return

$numpad4::
send {enter}/n track a{space}
return

$numpad5::
send {enter}/n track s{space}
return

$numpad7::
send {enter}/n cdr{space}
return

$numpad8::
send {enter}/n summs{space}
return

$numpad9::
send {enter}%clipboard%{enter}
return

$numpad0::
send {enter}/n summs{enter}
Sleep, 200
send {enter}%clipboard%{enter}
return

return
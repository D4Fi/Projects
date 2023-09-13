func Css(pat)
	let c = nr2char(getchar(0))
	return (c =~ a:pat) ? '' : c
endfunc


"autocomplet css ###################################################
iabbrev width width: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
iabbrev height height: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
iabbrev margin margin: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
iabbrev padding padding: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
iabbrev display display: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
iabbrev border border: 1px solid @;<esc><Home>f@s<c-r>=Css('\s')<cr>
iabbrev color color: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"iabbrev flex-direction flex-direction: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev flex-wrap flex-wrap: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev flex-flow flex-flow: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev justify-content justify-content: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev align-items align-items: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev align-content align-content: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev order order: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev flex-grow flex-grow: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"'#'iabbrev flex-shrink flex-shrink: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev flex flex: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"#iabbrev align-self align-self: @;<esc><Home>f@s<c-r>=Css('\s')<cr>
"iabbrev : @;<esc><Home >f@s<c-r>=Css('\s')<cr>

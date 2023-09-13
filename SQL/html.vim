set tabstop=2 
set softtabstop=2 
set shiftwidth=2

func Html(pat)
	let c = nr2char(getchar(0))
	return (c =~ a:pat) ? '' : c
endfunc

" Autocomplet html  ########################################################
iabbrev class class="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev id id="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev id id="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev name name="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev method method="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev content content="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev span span="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev href href="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev src src="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev lang lang="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev title title="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev alt alt="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev hidden hidden="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev width width="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev height height="@"<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev h1 <h1>@</h1><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev h2 <h2>@</h2><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev h3 <h3>@</h3><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev h4 <h4>@</h4><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev h5 <h5>@</h5><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev h6 <h6>@</h6><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev section <section>@</section><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev div <div>@</div><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev button <button>@</button><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev a <a>@</a><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev p <p>@</p><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev footer <footer>@</footer><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev style <style>@</style><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev php <php>@</php><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev li <li>@</li><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev ol <ol>@</ol><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev ul <ul>@</ul><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev span <span>@</span><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev head <head>@</head><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev body <body>@</body><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev main <main>@</main><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev aside <aside>@</aside><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev article <article>@</article><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev header <header>@</header><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev nav <nav>@</nav><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev span <span>@</span><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev pre <pre>@</pre><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev i <i>@</i><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev b <b>@</b><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev br </br>@<esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev hr </hr><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev img <img src="@" alt=""><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev source <source src="@" type=""><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev video <video>@</video><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev audio <audio>@</audio><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev iframe <iframe>@</iframe><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev input <input type="">@</ul><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev script <script>@</script><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev table <table>@</table><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev tr <tr>@</tr><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev td <td>@</td><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev thead <thead>@</thead><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev tbody <tbody>@</tbody><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev tfooter <tfooter>@</tfooter><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev u <u>@</u><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev strong <strong>@</strong><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev em <em>@</em><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev mark <mark>@</mark><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev smal <smal>@</smal><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev del <del>@</del><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev ins <ins>@</ins><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev sup <sup>@</sup><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev sub <sub>@</sub><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev th <th>@</th><esc><Home>f@s<c-r>=Html('\s')<cr>
"##########################################################################


"HTML snippds #############################################################
iabbrev refresh <meta http-equiv="refresh" content="1"/><esc><Home>f@s<c-r>=Html('\s')<cr>
iabbrev bootstrap <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"><c-r>=Html('\s')<cr>
iabbrev html 
			\<!DOCTYPE html><cr>
			\<html lang="en"><cr>
			\<head><cr>
			\<meta charset="UTF-8"><cr>
			\<meta name="viewport" content="width=device-width, initial-scale=1.0"><cr>
			\<meta http-equiv="X-UA-Compatible" content="ie=edge"><cr>
			\<title>HTML 5 Boilerplate</title><cr>
			\<link rel="stylesheet" href="style.css"><cr>
			\</head><cr>
			\<body><cr>
			\<script src="index.js"></script><cr>
			\</body><cr>
			\</html>
"##########################################################################

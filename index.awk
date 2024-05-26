BEGIN {
    FS = "/"
    levelindent = 4
    split("*+-*+-*+-*+-*+-*+-",liststyle,//)
}
{
    sub(/^\.\//,"",$0)
    depth = NF-1
    filename = $(NF)
    path = $0; sub(/[^/]*$/,"",path)

    ## print each path part on first dir entry
    accpath = ""
    for ( d = 1; d <= depth; d++ ) {
        accpath = accpath $(d) "/"
        if ( ! seen[accpath]++ )
            printf("%*s %s %s\n", levelindent*(d-1), "", \
                liststyle[d], $(d) "/")
    }

    printf("%*s %s [%s](%s)\n", levelindent*(depth), "", \
        liststyle[depth+1], filename, base path filename)
}
#! /bin/sh -
# Read one or more HTML/SGML/XML files given on the command
# line containing markup like <tag>word</tag> and output on
# standard output a tab-separated list of
#
#       count word tag filename
#
# sorted by ascending word and tag.
#
# Usage:
#       taglist xml-files

process () {
  cat "$1" |
    # turn <systemitem role="url"> into <URL>
    sed -e 's#systemitem *role="url"#URL#g' -e 's#/systemitem#/URL#' |

      # turn punctuation into newlines
      tr ' (){}[]' '\n\n\n\n\n\n\n' |

        # select tagged words
        egrep '>[^<>]+</' |

  	# split <emphasis>XXX</emphasis> into "" emphasis XXX /emphasis
  	# print: word tag filename
          awk -F'[<>]' -v FILE="$1" \
              '{ printf("%-31s\t%-15s\t%s\n", $3, $2, FILE) }' |

  	  # sort by word
            sort |

  	    # merge lines and precede with count
              uniq -c |

  	      # final formatting, add arrow if word is same as previous
                awk '{
                        print ($2 == Last) ? ($0 " <----") : $0
                        Last = $2
                     }'
}

for f in "$@"
do
    process "$f"
done

import fresh_tomatoes
import media


wonder_woman = media.Movie("Wonder Woman",
                           "Before she was Wonder Woman (Gal Gadot), she was Diana, princess of the Amazons, trained to be an unconquerable warrior. Raised on a sheltered island paradise, Diana meets an American pilot (Chris Pine) who tells her about the massive conflict that's raging in the outside world. Convinced that she can stop the threat, Diana leaves her home for the first time. Fighting alongside men in a war to end all wars, she finally discovers her full powers and true destiny.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=F0lZgaz0CIE")

pirates = media.Movie("Pirates of the Caribbean",
                      "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the evil Capt. Salazar, escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British navy.",
                      "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
                      "https://www.youtube.com/watch?v=fdK_vAd0EeI")

the_mummy = media.Movie("The Mummy",
                        "Nick Morton is a soldier of fortune who plunders ancient sites for timeless artifacts and sells them to the highest bidder. When Nick and his partner come under attack in the Middle East, the ensuing battle accidentally unearths Ahmanet, a betrayed Egyptian princess who was entombed under the desert for thousands of years. With her powers constantly evolving, Morton must now stop the resurrected monster as she embarks on a furious rampage through the streets of London.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",
                        "https://www.youtube.com/watch?v=SM0UP_HxPbw")               

baywatch = media.Movie("Baywatch",
                       "Matt Brody is a former Olympic swimmer who wants to join an elite team of lifeguards led by the hulking Mitch Buchannon. Brody thinks he's a shoo-in, but his casual attitude starts to instantly rub Mitch the wrong way. When drugs and a shady resort owner pose a threat to the bay, Mitch and Matt must put their differences aside to spring into action and save the day.",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Baywatch_poster.jpg",
                       "https://www.youtube.com/watch?v=oPu1Ejq__N0")

alien_covenant = media.Movie("Alien: Covenant",
                             "Bound for a remote planet on the far side of the galaxy, members (Katherine Waterston, Billy Crudup) of the colony ship Covenant discover what they think to be an uncharted paradise. While there, they meet David (Michael Fassbender), the synthetic survivor of the doomed Prometheus expedition. The mysterious world soon turns dark and dangerous when a hostile alien life-form forces the crew into a deadly fight for survival.",
                             "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
                             "https://www.youtube.com/watch?v=gIsxLgNVh70")

get_out = media.Movie("Get Out",
                      "Now that Chris (Daniel Kaluuya) and his girlfriend, Rose (Allison Williams), have reached the meet-the-parents milestone of dating, she invites him for a weekend getaway upstate with Missy and Dean. At first, Chris reads the family's overly accommodating behavior as nervous attempts to deal with their daughter's interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he never could have imagined.",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=y1gQ7RyvgXU")

guardians = media.Movie("Guardians of the Galaxy Vol 2",
                        "Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect their precious batteries from invaders. When it is discovered that Rocket has stolen the items they were sent to guard, the Sovereign dispatch their armada to search for vengeance. As the Guardians try to escape, the mystery of Peter's parentage is revealed.",
                        "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                        "https://www.youtube.com/watch?v=h7GiAwK2-fY")

captain_underpants = media.Movie("Captain Underpants",
                                 "George Beard and Harold Hutchins are two overly imaginative pranksters who spend hours in a treehouse creating comic books. When their mean principal threatens to separate them into different classes, the mischievous boys accidentally hypnotize him into thinking that he's a ridiculously enthusiastic, incredibly dimwitted superhero named Captain Underpants.",
                                 "https://upload.wikimedia.org/wikipedia/en/2/24/Captain_Underpants_The_First_Epic_Movie_poster.jpg",
                                 "https://www.youtube.com/watch?v=nenNgl8t-qU")

movies = [wonder_woman, pirates, the_mummy, baywatch, alien_covenant, get_out, guardians, captain_underpants]

fresh_tomatoes.open_movies_page(movies)


package utils

import (
	"app_go/entity"

	"math/rand"
)

var Jokes = []entity.Joke{
	{Value: "Chuck Norris ripped soneone's mouth up and told them to SHUT UP."},
	{Value: "Chuck Norris killed a fat guy with a poisened candy bar. and yes u r stupid for not thinking of that."},
	{Value: "The Dali Lama said that violence is wrong. Chuck Norris backhanded him."},
	{Value: "Mario & Luigi are the result of Chuck Norris cutting Don Corleone in half with an atomic wedgy."},
	{Value: "Yahweh strictly adheres to Chuck Norris' first commandment: having no other gods before him."},
	{Value: "Chuck Norris won the showcase on The Price Is Right even after bidding over the actual retail price."},
	{Value: "Chuck Norris kicked-in The Amazing Kreskin's face. Thus proving a Chuck Norris attack to be an unpredictable life event."},
	{Value: "When Chuck Norris comes to an open door, he always closes it so he can then kick it the fuck in."},
	{Value: "Archaeologists in Egypt have recently discovered what may be the world's oldest Chuck Norris fact written " +
		"on the inside of a sarcophagus - translated from the ancient language, it reads 'Big Chuck is holding a gun " +
		"to my head and telling me to write this/Big Chuck is the lord of time travel/All hail Big Chuck'."},
	{Value: "In Soviet Russia, Chuck Norris drinks vodka and kills any asshole wearing those stupid furry hats."},
	{Value: "C'mon Chuck Norris isn't that great... if he was truly that amazing he would come over and slam my head " +
		"into the key EAOJ;BGWoenbsKFDPONBqegkbs dlvjbasvaxfl;bxs spkadgo;kjsfbvklndsfalkmbnasdflkgbsadg;lkbsafd;" +
		"lkgbsad;glknb ;sldg"},
	{Value: "Chuck Norris built a time machine and went back in time to stop the JFK assassination. As Oswald shot, " +
		"Chuck Norris met all three bullets with his beard, deflecting them. JFK's head exploded out of sheer amazement."},
	{Value: "Chuck Norris is a bulldozer with a beard."},
	{Value: "you know how eyes are windows to the soul ? well if you have a staring contest with Chuck Norris he'll suck out your soul"},
	{Value: "Chuck Norris is friends with Sonic The Hedgehog. They race often, too. Unsurprisingly, Sonic loses every time he doesn't cheat."},
	{Value: "Chuck Norris just roundhouse kicked billy ray cyrus for mileys twerking"},
	{Value: "Inspired by Robert De Niro in Taxi Driver, Chuck Norris always keeps two spring-out M16s up the sleeves of his jackets."},
	{Value: "Little Johnny's teacher asked him to describe Chuck Norris. Little Johnny said Chuck Norris is like a wheelbarrow full of awesome."},
	{Value: "Chuck Norris likes his ice like he likes his skulls: crushed."},
	{Value: "Chuck Norris blows up ballons with his nose"},
}

func GetRandomJoke() entity.Joke {
	return Jokes[rand.Intn(len(Jokes))]
}

def format_episode(request, response, candidates, resp_persona_traits=None, resp_persona_prefix="",
                   candidates_random=None):
    """ Serializer for the deprecated formatter proposed by Facebook.
    """
    assert(isinstance(request, str))
    assert(isinstance(response, str))
    assert(isinstance(candidates, list))

    rand = None

    # Performing candidates shuffling
    if candidates_random is not None:
        candidates_random.shuffle(candidates)

    def __handle_line(l):
        return l.replace('\t', ' ')

    def __fn(a):
        return filter(lambda item: item is not None, a)

    lines = []

    if resp_persona_traits is not None:
        traits = ["{p}persona: {t}".format(
                    p=resp_persona_prefix, t="I am {}".format(__handle_line(t)) if t is not None else "none")
                  for t in resp_persona_traits]

        if rand is not None:
            rand.shuffle(traits)

        lines.extend(traits)

    # Main episode content. (Query - Response)
    text = "\n".join(__fn([__handle_line(request)]))
    labels = "\n".join([__handle_line(response)])
    reward = ""
    label_candidates = "|".join([__handle_line(c) for c in candidates])

    lines.append("\t".join([text, labels, reward, label_candidates]))

    return "\n".join(["{} {}".format(i+1, l) for i, l in enumerate(lines)])

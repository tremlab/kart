import React from 'react';
import SuggItem from './SuggItem.jsx';


const Suggestions = (props) => {
	const suggestions = props.suggestions;

	if (suggestions.length === 0) {
		return (
      <datalist id="suggestions">
          <option value="--no matches found"/>
      </datalist>
		)
	} else {
    const suggOptions = suggestions.map((sugg, i) =>
    	<SuggItem suggItem={sugg} key={`${sugg}-${i}`}/>
    )
		return (
      <datalist id="suggestions">
        { suggOptions }
      </datalist>
		)
	}
}

export default Suggestions;
